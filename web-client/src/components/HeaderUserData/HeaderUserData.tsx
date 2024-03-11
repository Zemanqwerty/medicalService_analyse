import { observer } from "mobx-react-lite";
import React, { FC, useContext } from "react";
import styles from './HeaderUserData.module.css';
import { Context } from "../..";

const HeaderUserData: FC = () => {
    const {store} = useContext(Context);

    return (
        <div className={styles.userDataBlock}>
            <div className={styles.userData}>
                <p>Вы вошли как</p>
                <p className={styles.userInfo}>{store.user.lastname} {store.user.firstname} {store.user.report}</p>
            </div>
            <button className={styles.logoutbtn} onClick={() => store.logout()}>Выйти</button>
        </div>
    )
};

export default observer(HeaderUserData);