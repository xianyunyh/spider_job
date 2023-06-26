import { Context } from 'koa';

// @ts-ignore
import Job, {analyticGroup} from '../models/job';

async function PostJob(ctx: Context) {
    const data: any = ctx.request.body
    ctx.log.debug(data)
    await Job.create({...data})
    ctx.response.body = {};
}
async function JobIndex(ctx: Context) {
    const group = ctx.params.group || 'experience';
    const res = await analyticGroup(group as string)
    ctx.log.debug(res)
    await ctx.render('analytic', { 
        title: group == 'experience' ? '工作经验分析' : "学历分析",
        groupText: group == 'experience' ? '工作经验' : "学历",
        group: group,
        data:res,
        chart:{
            salaryOption: {
                title: ''
            }
        } 
    })
}
export default {
    JobIndex,
    PostJob
}