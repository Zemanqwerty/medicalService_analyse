import React, {FC, memo, useContext, useEffect, useState} from "react";
import { Context } from "../..";
import { observable } from "mobx";
import { observer } from "mobx-react-lite";
import SendFileForm from "../../components/SendFileForm/SendFileForm";
import styles from './LKPage.module.css'
import AnalyseService from "../../services/AnalyseService";
import { Analyse } from "../../models/Analyse";
import AnalyseResults from "../../components/AnalyseResults";
import { useNavigate } from "react-router-dom";

const LKPage: FC = () => {

    const navigate = useNavigate();

    const {store} = useContext(Context);
    const [analyses, setAnalyses] = useState<Analyse[]>([]);
    
    useEffect(() => {
        if (!localStorage.getItem('token')) {
            return navigate("/login");
        }

        const getAnalyseData = async () => {
            const response = await AnalyseService.getAnalyse();
            console.log(response);
            setAnalyses(response.data)
        }

        getAnalyseData();
    }, [store.isAuth, navigate]);


    return (
        <>
            <div className={styles.main_wrapper}>
                {analyses.map(analyse => 
                    <AnalyseResults analyse={analyse} />
                )}
            </div>
        </>
    )
}

export default observer(LKPage);