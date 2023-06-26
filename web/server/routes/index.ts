import Router from '@koa/router';
import Job from '../controller/job'
import Api from '../api'
const router = new Router();
function registerAllRoutes(router: Router) {
  router.get("/job/analytic/:group", Job.JobIndex)
  router.post('/job', Job.PostJob)
  router.get('/api/analytic', Api.analytic)
}
registerAllRoutes(router);
export { router };
