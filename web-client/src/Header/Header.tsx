import React, {FC, memo, useContext, useState} from "react";
import { observable } from "mobx";
import { observer } from "mobx-react-lite";
import { Link } from "react-router-dom";
import styles from './Header.module.css'

const Header: FC = () => {

    return (
        <>
            <ul className={styles.ul_wrapper}>
                <li className={styles.li_default}>
                    <Link to="/" className={styles.li_default}>Главная</Link>
                </li>
                <li className={styles.li_default}>
                    <Link to="/login" className={styles.li_default}>Личный кабинет</Link>
                </li>
            </ul>
        </>
    )
}

export default observer(Header);