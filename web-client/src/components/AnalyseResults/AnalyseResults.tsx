import React, {FC, memo, useContext, useState} from "react";
import { observable } from "mobx";
import { observer } from "mobx-react-lite";
import { Link } from "react-router-dom";
import styles from './AnalyseResults.module.css'
import AnalyseData from "../AnalyseData";
import showArrow from '../../sources/images/Arrow.png';

interface PromptTypes {
    anayse: {info_1: string, info_2: string, filename: string}
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
        <>
            <div className={styles.blockWrapper}>
                <div className={styles.btnWrapperBlock} onClick={showData}>
                    <p>{props.anayse.filename}</p>
                    <img src={showArrow} alt="" style={{
                        transform: showResultData ? 'rotate(180deg)' : '',
                    }}/>
                </div>
                {showResultData === false ?
                null :
                <AnalyseData anayse={props.anayse}/>}
            </div>
        </>
    )
}

export default observer(AnalyseResult);