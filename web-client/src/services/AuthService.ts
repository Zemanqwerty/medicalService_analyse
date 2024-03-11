import { AxiosResponse } from "axios";
import $api from "../http";
import { AuthResponse } from "../models/response/AuthResponse";

export default class AuthService {
    static async login(first_name: string, last_name: string, report: string, password: string): Promise<AxiosResponse<AuthResponse>> {
        return $api.post<AuthResponse>('auth/sign-in', {first_name, last_name, report, password});
    }

    // static async registration(username: string, password: string): Promise<AxiosResponse<AuthResponse>> {
    //     return $api.post<AuthResponse>('auth/sign-up', {username, password});
    // }

    static async logout(): Promise<void> {
        return $api.get('/auth/logout');
    }
}