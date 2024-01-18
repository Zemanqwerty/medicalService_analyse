import React, {FC, useContext, useEffect, useState} from 'react';
import { Context } from '.';
import { observer } from 'mobx-react-lite';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import MainPage from './pages/mainPage/MainPage';
import LoginPage from './pages/LKPage';
import Header from './Header/Header';


const App: FC = () => {

  const {store} = useContext(Context);

  useEffect(() => {
    if (localStorage.getItem('token')) {
      store.checkAuth()
    }
  }, [])

  if (store.isLoading) {
    return (
      <>
      LOADING...
      </>
    )
  }

  return (
    <>
    
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/">
          <Route index element={<MainPage />} />
          <Route path="/login" element ={<LoginPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
    
    </>
  )
}

export default observer(App);