const request = require('@request');
const mysql = require('@mysql');

async function add_user(data) {
    let {body, statusCode} = await request('/', 'POST', data);
    return body.data.id
}

describe('Managament User', () => {

    test('Crear usuario OK con todos los campos válidos', async () => {
        let {body, statusCode} = await request('/', 'POST', {name: 'jose', last_name: 'Guillermo'});
        expect(statusCode).toEqual(200);
        expect(body.data.id).toBeDefined();
        expect(body).toEqual(
            {
                "code": 2000,
                "data": {
                    "id": body.data.id
                },
                "error": false,
                "message": "SUCCESS"
            });

        let results = await mysql(`SELECT name, last_name FROM user WHERE id = "${body.data.id}"`);
        expect(results[0].name).toEqual('jose');
        expect(results[0].last_name).toEqual('Guillermo');
    });

    test('Crear usuario OK sin el last_name: parametro no requerido', async () => {
        let {body, statusCode} = await request('/', 'POST', {name: 'jose'});
        expect(statusCode).toEqual(200);
        expect(body.data.id).toBeDefined();
        expect(body).toEqual(
            {
                "code": 2000,
                "data": {
                    "id": body.data.id
                },
                "error": false,
                "message": "SUCCESS"
            });

        let results = await mysql(`SELECT name, last_name FROM user WHERE id = "${body.data.id}"`);
        expect(results[0].name).toEqual('jose');
        expect(results[0].last_name).toEqual(null);
    });

    test('Crear Error: no se pasa el parametro requerido: nombre de usuario', async () => {
        let {body, statusCode} = await request('/', 'POST', {last_name: 'Guillermo'});
        expect(statusCode).toEqual(500);
        expect(body).toEqual({
            "code": 4000,
            "data": [],
            "error": true,
            "message": "El Nombre de usuario es requerido"
        });
    });

    test('Crear usuario ERROR el apellido tiene pocos caracteres', async () => {
        let {body, statusCode} = await request('/', 'POST', {name: 'jose', last_name: 'Gu'});
        expect(body).toEqual({
            "code": 4000,
            "data": [],
            "error": true,
            "message": "El apellido debe ser mayor a 3 caracteres"
        });
        expect(statusCode).toEqual(500);
    });

    test('Actualizar Error no existe le usuario', async () => {
        let {body, statusCode} = await request('/1', 'PUT', {name: 'jose',last_name: 'Guillermo'});
        expect(statusCode).toEqual(500);
        expect(body).toEqual({
            "code": 4000,
            "data": [],
            "error": true,
            "message": "No existe el usuario con id : 1"
        });
    });


    test('Actualizar Error, no se envian todos los parametros', async () => {

        id = await add_user({
            name: 'jose',
            last_name: 'Guillermo'
        });

        let {body, statusCode} = await request(`/${id}`, 'PUT', {names: 'jose'});
        expect(statusCode).toEqual(500);
        expect(body).toEqual({
            "code": 4000,
            "data": [],
            "error": true,
            "message":
                "El Nombre de usuario es requerido"
        });
    });

    test('Update Ok con todos los campos', async () => {
        id = await add_user({
            name: 'jose',
            last_name: 'Guillermo'
        });

        let {body, statusCode} = await request(`/${id}`, 'PUT', {name: 'Antonio', last_name: 'Inche'});

        expect(body).toEqual({
            "code": 2000,
            "data": "ok",
            "error": false,
            "message": "SUCCESS"
        });
        expect(statusCode).toEqual(200);

        let results = await mysql(`SELECT name, last_name FROM user WHERE id = "${id}"`);
        expect(results[0].name).toEqual('Antonio');
        expect(results[0].last_name).toEqual('Inche');


    });

});


describe('List User', () => {
    test('listar un usuario que no existe', async () => {
        let {body, statusCode} = await request('/156');
        expect(statusCode).toEqual(500);
        expect(body).toEqual({
            "message": "No existe el usuario con id : 156",
            "code": 4000,
            "error": true,
            "data": []
        });
    });

    test('listar un usuario existe', async () => {

        id = await add_user({
            name: 'jose',
            last_name: 'Guillermo'
        });

        let {body, statusCode} = await request(`/${id}`, 'GET');
        expect(statusCode).toEqual(200);
        expect(body).toEqual({
            "code": 2000,
            "data": {
                "id": id,
                "last_name": "Guillermo",
                "name": "jose"
            },
            "error": false,
            "message": "SUCCESS"
        });
    });
});

describe('List Collection User', () => {
    test('listar todos los usuarios', async () => {
        let rng = Math.floor((Math.random() * 9999) + 1);
        id = await add_user({
            name: 'jose',
            last_name: 'Inche' + rng
        });
        let {body, statusCode} = await request(`/?last_name=inche${rng}`);
        expect(body).toEqual({
            "message": "SUCCESS",
            "code": 2000,
            "error": false,
            "data": [
                {
                    "id": id,
                    "last_name": "Inche" + rng,
                    "name": "jose"
                }
            ]
        });
        expect(statusCode).toEqual(200);
    });
});

describe('connecion de la base de datos', () => {
    test('listar todos los usuarios', async () => {

        let {body, statusCode} = await request(`/?last_name=inchedfhkjbjdhfbd`);
        expect(body).toEqual({
            "message": "SUCCESS",
            "code": 2000,
            "error": false,
            "data": [
            ]
        });
        expect(statusCode).toEqual(200);
    });
});

