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

    return (
        <>
                {props.analyse.reference_results.map(analyse => 
                    <div dangerouslySetInnerHTML={{__html: analyse}} className={styles.resAnalyse}></div>
                )}
        </>
    )
}

export default observer(AnalyseData);