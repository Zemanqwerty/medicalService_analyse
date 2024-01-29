import React, {FC, memo, useContext, useState} from "react";
import { observable } from "mobx";
import { observer } from "mobx-react-lite";
import { Link } from "react-router-dom";
import styles from './AnalyseData.module.css'

interface PromptTypes {
    analyse: {info_1: string, info_2: string, reference_results: string[]}
}

const AnalyseData: FC<PromptTypes> = (props) => {

    return (
        <>
                <div dangerouslySetInnerHTML={{__html: props.analyse.info_1}}></div>
                <div dangerouslySetInnerHTML={{__html: props.analyse.info_2}}></div>
                {props.analyse.reference_results.map(analyse => 
                    <div dangerouslySetInnerHTML={{__html: analyse}} className={styles.resAnalyse}></div>
                )}
        </>
    )
}

export default observer(AnalyseData);