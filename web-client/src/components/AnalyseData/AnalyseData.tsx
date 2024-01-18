import React, {FC, memo, useContext, useState} from "react";
import { observable } from "mobx";
import { observer } from "mobx-react-lite";
import { Link } from "react-router-dom";
// import styles from './'

interface PromptTypes {
    anayse: {info_1: string, info_2: string}
}

const AnalyseData: FC<PromptTypes> = (props) => {

    return (
        <>
                <div dangerouslySetInnerHTML={{__html: props.anayse.info_1}}></div>
                <div dangerouslySetInnerHTML={{__html: props.anayse.info_2}}></div>
        </>
    )
}

export default observer(AnalyseData);