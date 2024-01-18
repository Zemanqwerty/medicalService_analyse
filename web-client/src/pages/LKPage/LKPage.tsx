import React, {FC, memo, useContext, useEffect, useState} from "react";
import { Context } from "../..";
import { observable } from "mobx";
import { observer } from "mobx-react-lite";
import SendFileForm from "../../components/SendFileForm/SendFileForm";
import styles from './LKPage.module.css'
import AnalyseService from "../../services/AnalyseService";
import { Analyse } from "../../models/Analyse";
import AnalyseResults from "../../components/AnalyseResults";

const LKPage: FC = () => {

    const {store} = useContext(Context);
    const [firstName, setFirstName] = useState<string>('');
    const [lastName, setLastName] = useState<string>('');
    const [report, setReport] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    const [analyses, setAnalyses] = useState<Analyse[]>([]);

    if (store.isAuth) {
        

        // useEffect(() => {
        //     const f = async () => {
        //         const response = await AnalyseService.getAnalyse();
        //         console.log(response.data);
        //         setAnalyses(response.data)
        //     }

        //     f()
        // }, []);

        const getAnalyseData = async () => {
            const response = await AnalyseService.getAnalyse();
            console.log(response);
            setAnalyses(response.data)
        }


        return (
            <>
                <div className={styles.main_wrapper}>
                <button onClick={getAnalyseData} className={styles.send_btn}>Получить результаты</button>

                {analyses.map(analyse => 
                    <AnalyseResults anayse={analyse} />
                )}
                </div>
            </>
        )
    }
    
    return (
        <>
            <div className={styles.main_wrapper}>
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
                <input type="text"  className={styles.input_default}
                    onChange={e => setPassword(e.target.value)}
                    placeholder="Пароль"
                    value={password}/>
                
                <button className={styles.send_btn} onClick={() => {
                        store.login(firstName, lastName, report, password);
                        }
                    }>Войти</button>
            </div>
        </>
    )
}

export default observer(LKPage);