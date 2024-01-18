import React, {FC, memo, useContext, useState} from "react";
import { Context } from "../..";
import { observable } from "mobx";
import { observer } from "mobx-react-lite";
import SendFileForm from "../../components/SendFileForm/SendFileForm";

const MainPage: FC = () => {

    const {store} = useContext(Context);

    return (
        <>
            <SendFileForm />
        </>
    )
}

export default observer(MainPage);