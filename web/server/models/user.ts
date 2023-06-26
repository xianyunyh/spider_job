import { DataTypes } from 'sequelize';
import sequelize from './database'
const User = sequelize.define('users', {
    user_name: DataTypes.STRING,
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true,
    },
}, {
    timestamps: false,
});
User.sync();
export default User;