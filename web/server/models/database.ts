import { Sequelize } from 'sequelize'
import conf from '../config/index';
import type {Options } from 'sequelize';
const database = conf.database as Options
const sequelize = new Sequelize({
  ...database
});
sequelize.authenticate().then(() => {
  console.log("connect success") 
  sequelize.sync()
}).catch(() => {
  console.log("connect databse failed")
})
export const init = async () => {}
export default sequelize;