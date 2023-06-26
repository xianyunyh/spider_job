import { Context } from 'koa';

import User from '../models/user';
async function GetIndex(ctx: Context) {
    ctx.log.info("GetIndex")
    await User.create(
        {
            user_name: "test",
        }
    )
    await ctx.render("index", { title: "Hello Koa 2!" })
}
export default {
    GetIndex
}