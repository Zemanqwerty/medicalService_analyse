import React, {FC, memo, useContext, useState} from "react";
import { observable } from "mobx";
import { observer } from "mobx-react-lite";
import { Link } from "react-router-dom";
import styles from './Header.module.css'
import { Context } from "../.";
import HeaderUserData from "../components/HeaderUserData";

const Header: FC = () => {
    const {store} = useContext(Context);

    return (
        <div className={styles.headerWrapper}>
            <div className={styles.header}>
                <ul className={styles.ul_wrapper}>
                    <li className={styles.li_default}>
                        <Link to="/" className={styles.li_default}>Главная</Link>
                    </li>
                    <li className={styles.li_default}>
                        <Link to="/login" className={styles.li_default}>Личный кабинет</Link>
                    </li>
                </ul>
                {store.isAuth ? <HeaderUserData /> : null}
            </div>
        </div>
    )
}

export default observer(Header);