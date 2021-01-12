import React, { Component } from "react";
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Typography from '@material-ui/core/Typography';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import FiberManualRecordIcon from '@material-ui/icons/FiberManualRecord';
import Box from '@material-ui/core/Box';

export default function Home(){
    //const { searchTitle, tutorials, currentTutorial, currentIndex } = this.state;
    return (
    <div align="center">
        <Box
        boxShadow={2}
        bgcolor="background.paper"
        m={1}
        p={1}
        style={{ width: '50%',marginTop:'3rem'}}
      >
        <List>
                <ListItem >
                    <ListItemText
                        primary={
                        <Typography fontWeight="fontWeightBold" variant="h5">
                            <b>Django + React (aplikacja CRUD)</b>
                        </Typography>
                        }
                    />
                </ListItem>
                <ListItem >
                    <ListItemIcon>
                        <FiberManualRecordIcon/>
                    </ListItemIcon>
                    <ListItemText
                        primary="frontend napisany za pomocą React.js,"
                    />
                </ListItem>
                <ListItem >
                    <ListItemIcon>
                        <FiberManualRecordIcon/>
                    </ListItemIcon>
                    <ListItemText
                        primary="biblioteka ‘axios’ użyta do “konsumowania” API wystawionego np. przez DRF,"
                    />
                </ListItem>
                <ListItem >
                    <ListItemIcon>
                        <FiberManualRecordIcon/>
                    </ListItemIcon>
                    <ListItemText
                        primary="przykład aplikacji CRUD z wykorzystaniem Django i React’a,"
                    />
                </ListItem>
                <ListItem >
                    <ListItemIcon>
                        <FiberManualRecordIcon/>
                    </ListItemIcon>
                    <ListItemText
                        primary="należy przeanalizować i wdrożyć kod z ww. poradnika,"
                    />
                </ListItem>
                <ListItem >
                    <ListItemIcon>
                        <FiberManualRecordIcon/>
                    </ListItemIcon>
                    <ListItemText
                        primary="plusy za własne przemyślenia, analizę dokumentacji i idące za nimi modyfikacje w aplikacji."
                    />
                </ListItem>
            </List>
      </Box>


        
    </div>
    );
}

/*  backend napisany w Django,
                        frontend napisany za pomocą React.js,
                        biblioteka ‘axios’ użyta do “konsumowania” API wystawionego np. przez DRF,
                        przykład aplikacji CRUD z wykorzystaniem Django i React’a,
                        należy przeanalizować i wdrożyć kod z ww. poradnika,
                        plusy za własne przemyślenia, analizę dokumentacji i idące za nimi modyfikacje w aplikacji. 
                    */