import React, {FC, memo, useContext, useState} from "react";
import { observable } from "mobx";
import { observer } from "mobx-react-lite";
import { Link } from "react-router-dom";
import styles from './AnalyseData.module.css'
import DataFrameTable from "../DataFrameTable";

interface PromptTypes {
    analyse: {info_1: string, info_2: string, reference_results: string[], main_frame: string}
}

const AnalyseData: FC<PromptTypes> = (props) => {

    if (props.analyse.info_1 === props.analyse.reference_results[0] || props.analyse.info_2 === props.analyse.reference_results[0]) {
        props.analyse.reference_results[0] = '';
    }

    return (
        <>
                <div dangerouslySetInnerHTML={{__html: props.analyse.info_1}}></div>
                <div dangerouslySetInnerHTML={{__html: props.analyse.info_2}}></div>
                <hr />
                {props.analyse.main_frame === 'Нет отрицательных результатов' ? props.analyse.main_frame : <DataFrameTable dataframe={props.analyse.main_frame} />}
                {props.analyse.reference_results[0] !== '' ? <hr /> : ''}
                {props.analyse.reference_results.map(analyse => 
                    <div dangerouslySetInnerHTML={{__html: analyse}} className={styles.resAnalyse}></div>
                )}
        </>
    )
}

export default observer(AnalyseData);