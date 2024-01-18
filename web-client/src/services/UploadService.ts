import { AxiosResponse } from "axios";
import $api from "../http";
import { AuthResponse } from "../models/response/AuthResponse";
// import { UploadResponse } from "src/models/response/UploadResponse";

export default class UploadService {
    static async upload(first_name: string, last_name: string, report: string, age: number, sex: string, files: File[]): Promise<AxiosResponse<{message: string}>> {
        
        const formData = new FormData();
        // formData.append("file", file);

        // files.map((file, index) => (
        //     formData.append(`file_${index}`, file)
        // ))

        for (let fileIndex = 0; fileIndex < 12; fileIndex++) {
            try {
                formData.append(`file_${fileIndex+1}`, files[fileIndex])
            } catch (e) {
                formData.append(`file_${fileIndex+1}`, '')
            }
        }

        formData.append("first_name", first_name);
        formData.append("last_name", last_name);
        formData.append("report", report);
        formData.append("age", `${age}`);
        formData.append("sex", sex);


        return $api.post<any>('/upload', formData, {headers: {
            "content-type": "multipart/form-data",
        }});
    }

    // static async registration(username: string, password: string): Promise<AxiosResponse<AuthResponse>> {
    //     return $api.post<AuthResponse>('auth/sign-up', {username, password});
    // }

    // static async logout(): Promise<void> {
    //     return $api.get('/auth/logout');
    // }
}