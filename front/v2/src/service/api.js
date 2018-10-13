import request from '@/service/request'
const base_url = 'http://yehe.37he.cn/api/'
const get_weekline_url = base_url + '/weekdayline.php'
export const get_week_line =  (data)=>  request.get(get_weekline_url,data)
export const get_work_year =  (data) => request.get(base_url + 'workyear.php',data)
export const get_education =  (data) => request.get(base_url + 'education.php',data)
export const get_wordcloud =  (data) => request.get(base_url + 'word.json',data)
export const get_hot_compay = (data) => request.get(base_url + 'company.php',data)
export const get_month_line = (data) => request.get(base_url + 'monthline.php',data)