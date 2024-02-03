import { observer } from "mobx-react-lite";
import React, { FC } from "react";
import styles from './DataFrameTable.module.css'

interface DataFrame {
    dataframe: string;
}

const DataFrameTable: FC<DataFrame> = (props) => {

    const frame_lines = props.dataframe.split('\n');

    return (
        <table>
            <tbody>
                {frame_lines.map((line, index) => {
                const splitedColumns = line.split(' ');
                const value = splitedColumns[splitedColumns.length - 1];
                const title = splitedColumns.slice(0, -1);
                title.shift()
                const columns = [title, value]
                return (
                    <tr key={index}>
                    {columns.map((column, colIndex) => (
                        column === '' ? null : <td className={styles.tableTd} key={colIndex}>{column}</td>
                    ))}
                    </tr>
                );
                })}
            </tbody>
        </table>
    )
};

export default observer(DataFrameTable);