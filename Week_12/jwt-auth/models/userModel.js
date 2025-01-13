const {db} = require('./config/db.js');
const bcrypt = require('bcrypt');

module.exports = {
    createUser: async(password, email) => {
        const trx = await db.transaction();

        try {
            // hash the password
            const hashPassword = await bcrypt.hash(password + "", 10);

            const [user] = await trx('users')
                .insert({
                    email: email.toLowerCase(),
                    password: hashPassword
                },
                ["email", "id"]
            );

            await trx.commit();

            return user;
        } catch (error) {
            await trx.rollback();
            console.error(error.message);
            throw error;
        }
    },
    getUserByEmail: async(email) => {
        try {
            const user = await db('users')
                .select("id", "email", "password")
                .where({email: email.toLowerCase()})
                .first();
            return user;
        } catch (error) {
            console.error(error.message);
            throw error;
        }
    },

    getUsers: async() => {
        try {
            const users = await db('users')
                .select("id", "email");
            return users;
        } catch (error) {
            console.error(error.message);
            throw error;
        }
    }
}