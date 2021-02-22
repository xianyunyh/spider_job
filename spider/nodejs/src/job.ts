export interface Salary {
    max: number;
    min: number;
    avg: number;
}


export interface CompanyInfo {
    company_id: string;//公司id
    company_name: string;//公司名称
    company_scale: string;//公司规模
    company_stage: string; //发展阶段
    company_area: string;//公司领域
    company_site: string;//公司网站
    position_lng: string;
    position_lat: string;

}
export interface JobItem {
    address: string;
    create_time: string;
    salary: Salary,
    body: string,
    company_name: string,
    postion_id: string,
    position_name: string,
    educational: string,
    work_year: string,
    from_site ?: string,
    company_info: CompanyInfo
}