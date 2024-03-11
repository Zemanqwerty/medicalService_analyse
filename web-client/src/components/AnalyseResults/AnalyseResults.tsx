import React, {FC, memo, useContext, useState} from "react";
import { observable } from "mobx";
import { observer } from "mobx-react-lite";
import { Link } from "react-router-dom";
import styles from './AnalyseResults.module.css'
import AnalyseData from "../AnalyseData";
import showArrow from '../../sources/images/Arrow.png';

interface PromptTypes {
    analyse: {info_1: string, info_2: string, reference_results: string[], filename: string, main_frame: string}
}

const AnalyseResult: FC<PromptTypes> = (props) => {
    
    const [showResultData, setShowResultData] = useState(false);

    const showData = () => {
        if (showResultData === true) {
            setShowResultData(false);
        } else {
            setShowResultData(true)
        }
    }

    return (
        <div className={styles.contentWrapper}>
            <div className={styles.blockWrapper}>
                <div className={styles.btnWrapperBlock} onClick={showData}>
                    <p>{props.analyse.filename}</p>
                    <img src={showArrow} alt="" className={styles.showInfoArrow} style={{
                        transform: showResultData ? 'rotate(180deg)' : '',
                    }}/>
                </div>
                {showResultData === false ?
                null :
                <AnalyseData analyse={props.analyse}/>}
            </div>
        </div>
    )
}

export default observer(AnalyseResult);