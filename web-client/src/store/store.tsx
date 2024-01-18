import axios from "axios";
import { IUser } from "../models/IUser";
import AuthService from "../services/AuthService";
import { makeAutoObservable } from "mobx";
import { AuthResponse } from "../models/response/AuthResponse";
import { API_URL } from "../http";

export default class Store {
    user = {} as IUser;
    isAuth = false;
    isLoading = false;
    response: string = '';

    constructor() {
        makeAutoObservable(this);
    }

    setAuth(bool: boolean) {
        this.isAuth = bool;
    }

    setUser(user: IUser) {
        this.user = user;
    }

    setResponse(message: string) {
        this.response = message;
    }

    setLoading(bool: boolean) {
        this.isLoading = bool;
    }



    async login(first_name: string, last_name: string, report: string, password: string) {
        try {
            const response = await AuthService.login(first_name, last_name, report, password);
            console.log(response);
            localStorage.setItem('token', response.data.access_token);
            this.setAuth(true);
            this.setUser(response.data.user);
        } catch (e) {
            console.log(e);
        }
    }

    // async registration(username: string, password: string) {
    //     try {
    //         const response = await AuthService.registration(username, password);
    //         localStorage.setItem('token', response.data.accessToken);
    //         this.setAuth(true);
    //         this.setUser(response.data.user);
    //     } catch (e) {
    //         console.log(e);
    //     }
    // }

    // async logout() {
    //     try {
    //         await AuthService.logout();
    //         localStorage.removeItem('token');
    //         this.setAuth(false);
    //         this.setUser({} as IUser);
    //     } catch (e) {
    //         console.log(e);
    //     }
    // }

    async checkAuth() {
        this.setLoading(true);
        try {
            const response = await axios.get<AuthResponse>(`${API_URL}/auth/refresh`, {withCredentials: true});

            localStorage.setItem('token', response.data.access_token);
            this.setAuth(true);
            this.setUser(response.data.user);
        } catch (e) {
            console.log(e);
        } finally {
            this.setLoading(false);
        }
    }
}