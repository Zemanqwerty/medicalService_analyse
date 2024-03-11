import { observer } from "mobx-react-lite";
import React, { FC } from "react";
import styles from './LoadingSpiner.module.css';

const LoadingSpiner: FC = () => {
    return (
        <div className={styles.loadingWrapper}>
            {/* <div className={styles.spinner}>
                <div className={`${styles.spinner_circle} ${styles.spinner_circle_outer}`}></div>
                <div className={`${styles.spinner_circle_off} ${styles.spinner_circle_inner}`}></div>
                <div className={`${styles.spinner_circle} ${styles.spinner_circle_single_1}`}></div>
                <div className={`${styles.spinner_circle} ${styles.spinner_circle_single_2}`}></div>
                <div className={styles.text}>Загужаем файлы...</div>
            </div> */}
            <div className={styles.cssload_weird}>	
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            <p className={styles.loadingTitle}>Анализируем файлы...</p>
        </div>
    )
};

export default observer(LoadingSpiner);