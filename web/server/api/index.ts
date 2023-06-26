import { Context } from 'koa';
import {analyticGroup} from '../models/job';
async function analytic(ctx: Context) {
    const group = ctx.query.group || 'experience';
    ctx.log.debug(group)
    const res = await analyticGroup(group as string)
    ctx.response.body = res; 
}
export default {
    analytic
}