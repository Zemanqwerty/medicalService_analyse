import { observer } from "mobx-react-lite";
import React, {ChangeEvent, FC, memo, useCallback, useContext, useState} from "react";
import { Context } from "../..";
import UploadService from "../../services/UploadService";
import styles from './SendFileForm.module.css'

const SendFileForm: FC = () => {
    const [firstName, setFirstName] = useState<string>('');
    const [lastName, setLastName] = useState<string>('');
    const [report, setReport] = useState<string>('');
    const [age, setAge] = useState<any>(null);
    const [sex, setSex] = useState<string>('');
    const [file, setFile] = useState<any>(null);
    const [files, setFiles] = useState<File[]>([]);

    const [response, setResponse] = useState<string>("")

    const {store} = useContext(Context)

    const sendFile = () => {
        console.log(files);
        const uploadResponse = UploadService.upload(firstName, lastName, report, age, sex, files).then((response) => {
            console.log(response);
            if(response?.status == 200){
                setResponse(response.data.message)
                setFirstName('');
                setLastName('');
                setReport('');
                setAge(null);
                setSex('');
            } else {
                setResponse('Некорректный формат файла')
            }
        })
    }
    
    const handleFilesChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files) {
            if (files.length >= 12) {
                setResponse('Выбрано максимальное количество файлов');
                return
            }
            setFiles(Array.from(e.target.files).concat(files));
        }
    };

    return (
        <>
            <div className={styles.main_wrapper}>
                <div className="">{response}</div>
                <input type="text" className={styles.input_default}
                    onChange={e => setFirstName(e.target.value)}
                    placeholder="Имя"
                    value={firstName}/>
                <input type="text" className={styles.input_default}
                    onChange={e => setLastName(e.target.value)}
                    placeholder="Фамилия"
                    value={lastName}/>
                <input type="text"  className={styles.input_default}
                    onChange={e => setReport(e.target.value)}
                    placeholder="Отчество"
                    value={report}/>
                <input type="text"  className={styles.input_default}
                    onChange={e => setAge(e.target.value)}
                    placeholder="Возраст"
                    value={age}/>
                <input type="text"  className={styles.input_default}
                    onChange={e => setSex(e.target.value)}
                    placeholder="Пол (М/Ж)"
                    value={sex}/>
                
                <p>Вы можете выбрать до 12 файлов ({files.length} выбрано)</p>

                <input type="file" multiple onChange={handleFilesChange} />

                <ul className={styles.filesList}>
                    {files.map((file, index) => (
                    <li key={index}>{index + 1}) {file.name}</li>
                    ))}
                </ul>

                <button className={styles.send_btn} onClick={() => {
                    // UploadService.upload(firstName, lastName, report, age, sex, file);
                    sendFile();
                    }
                }>Отправить</button>

            </div>
        </>
    )
};

export default observer(SendFileForm);