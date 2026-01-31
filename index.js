// import React from 'react';
// import ReactDOM from 'react-dom';
// import { ThemeProvider } from '@mui/material/styles';
// import {CssBaseline} from '@mui/material';
// import 'aos/dist/aos';

// import theme from './theme/theme';
// import App from './App';

// ReactDOM.render(
//   <ThemeProvider theme={theme}>
//     <CssBaseline />
//     <App />
//   </ThemeProvider>,
//   document.getElementById('root')
// );


import React from 'react';
import { createRoot } from 'react-dom/client';
import { ThemeProvider } from '@mui/material/styles';
import { CssBaseline } from '@mui/material';
import theme from './theme/theme';
import App from './App';

const container = document.getElementById('root');
const root = createRoot(container);

root.render(
  <ThemeProvider theme={theme}>
    <CssBaseline />
    <App />
  </ThemeProvider>
);
