import axios from "axios";
import { JobItem } from "../spider/types";

const request = axios.create({
    baseURL: "http://127.0.0.1:3000"
})

export const postJob = async (job: JobItem) => {
    return request.post("/job", job)
}