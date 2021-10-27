import React from "react";
import { Line } from 'react-chartjs-2'
import GaugeChart from 'react-gauge-chart'

import './Charts.css'
const Charts = () => {
    return(
        <>
    <div className="Top-side-part">
    <div className="chart-distancia">
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
         <div className="chart-tempGauger">
         <GaugeChart id="gauge-chart2" 
            nrOfLevels={20} 
            percent={0.86} 
            />
         </div>
         </div>
         </>
    )
}
export default Charts;