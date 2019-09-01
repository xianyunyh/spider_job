import request from '@/service/request'

export const get_week_line =  (data)=>  request.get("/position/weekly",data)
export const get_work_year =  (data) => request.get('/position/work_year',data)
export const get_education =  (data) => request.get('/position/edu',data)
export const get_wordcloud =  (data) => request.get('/word',data)
export const get_hot_compay = (data) => request.get('/company/hot',data)
export const get_month_line = (data) => request.get('/position/monthly',data)
export const get_company_map = (data) => request.get('/company',data)
export const get_company_analysis = (data) => request.get('/company/analysis',data)