import { DataTypes, QueryTypes } from 'sequelize';
import sequelize from './database'
export interface Salary {
    max: number;
    min: number;
    avg: number;
}
const Job = sequelize.define('job', {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true,
    },
    job_id: {
        type: DataTypes.STRING,
        unique: true,
    },
    job_name: DataTypes.STRING,
    job_url: DataTypes.STRING,
    experience: DataTypes.STRING,
    educational: DataTypes.STRING,
    area: DataTypes.STRING,
    address: DataTypes.STRING,
    salary: DataTypes.JSON,
    body: DataTypes.TEXT,
    site: DataTypes.STRING,
    skill: DataTypes.JSON,
    company: DataTypes.JSON,
}, {
    timestamps: false,
});
Job.sync();

export const analyticGroup = async (group: string='experience') => {
    const sql = `SELECT ${group} as 'group' ,count(1) as count,AVG(salary->'$.avg') as salary from jobs GROUP BY ${group}`;
    const res = await sequelize.query(sql,{type: QueryTypes.SELECT});
    return res;
 }
export default Job;