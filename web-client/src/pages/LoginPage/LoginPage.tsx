import React, {FC, memo, useContext, useEffect, useState} from "react";
import { observable } from "mobx";
import { observer } from "mobx-react-lite";
import { Link, useNavigate } from "react-router-dom";
import styles from './LoginPage.module.css'
import { Context } from "../..";

const LoginPage: FC = () => {

    const navigate = useNavigate();

    const {store} = useContext(Context);
    const [firstName, setFirstName] = useState<string>('');
    const [lastName, setLastName] = useState<string>('');
    const [report, setReport] = useState<string>('');
    const [password, setPassword] = useState<string>('');

    useEffect(() => {
        if (localStorage.getItem('token')) {
            navigate("/lk");
        }
    }, [store.isAuth, navigate]);

    return (
        <>
             <div className={styles.main_wrapper}>
                <div className={styles.sendFileFormWrapper}>
                    <input type="text" className={styles.input_default}
                        onChange={e => setFirstName(e.target.value)}
                        placeholder="Имя"
                        value={firstName}/>
                    <input type="text"  className={styles.input_default}
                        onChange={e => setLastName(e.target.value)}
                        placeholder="Фамилия"
                        value={lastName}/>
                    <input type="text"  className={styles.input_default}
                        onChange={e => setReport(e.target.value)}
                        placeholder="Отчество"
                        value={report}/>
                    <input type="password"  className={styles.input_default}
                        onChange={e => setPassword(e.target.value)}
                        placeholder="Пароль"
                        value={password}/>
                    
                    <button className={styles.send_btn} onClick={() => {
                            store.login(firstName, lastName, report, password);
                            }
                        }>Войти</button>
                </div>
             </div>
        </>
    )
}

export default observer(LoginPage);