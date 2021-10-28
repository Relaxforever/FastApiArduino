import React, { useEffect, useState } from "react";
import { Line } from 'react-chartjs-2'
import GaugeChart from 'react-gauge-chart'

import './Charts.css'
import axios from 'axios';

const GetDataDisTemp = async (setDistancia) => {
    try {
        const resp = await axios.get('https://fastapiarduino.herokuapp.com/api/arduino/',{ headers: {
            
         }});
        setDistancia(resp.data.body);
    } catch (err) {
        // Handle Error Here
        console.error(err);
    }
};

const Charts = () => {
     const  [distancia, setDistancia] = useState(null);
     useEffect(() => {
         const get_DataInterval = setInterval(() => {
            GetDataDisTemp(setDistancia);
            
         }, 20500)
         return () => clearInterval(get_DataInterval);
      })
    //GetDataDisTemp();
    
     if (distancia){
        console.log(distancia[distancia.length - 1])
        var result = distancia.map(datos => (datos.distance))
        console.log(result)
     } 
    return(
        <>
    <div className="Top-side-part">
    <div className="chart-grafico">
        <Line
        data={{
            labels: ['dist 1', 'dist 2', 'dist 3'],
            datasets: [{
                label: 'Distancia', 
                data: [0, 59, 75],
                fill: false,
                borderColor: 'rgba(220, 65, 65, 1)',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderWidth: 1
            }]
        }}
        legend={{position: 'top'}}
        />
         </div>
         <div className="chart-grafico">
         <GaugeChart id="gauge-chart2" 
            nrOfLevels={40}
            animate={false}
            percent={distancia ? distancia[distancia.length - 1].temp / 40 : 0 / 40 } 
            />
            <div className="chart-Texto"><p>la ultima temperatura Registrada fue de {distancia ? distancia[distancia.length - 1].temp : 0}°</p></div>
         </div>
         </div>
         </>
    )
}
export default Charts;