import { AxiosResponse } from "axios";
import $api from "../http";
import { AuthResponse } from "../models/response/AuthResponse";
import { Analyse } from "../models/Analyse";
// import { UploadResponse } from "src/models/response/UploadResponse";

export default class AnalyseService {
    static async getAnalyse(): Promise<AxiosResponse<Analyse[]>> {
        return $api.get<Analyse[]>('/lk');
    }

    // static async registration(username: string, password: string): Promise<AxiosResponse<AuthResponse>> {
    //     return $api.post<AuthResponse>('auth/sign-up', {username, password});
    // }

    // static async logout(): Promise<void> {
    //     return $api.get('/auth/logout');
    // }
}