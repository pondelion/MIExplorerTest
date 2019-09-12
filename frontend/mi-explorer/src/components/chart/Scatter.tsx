import React from 'react';
import request from 'superagent';
import { Scatter as ChartScatter } from 'react-chartjs-2';

type Props= {}

export class Scatter extends React.Component<Props> {

  private _data: any = null;
  private _label = [];

  constructor(props: Props) {
    super(props);

    this._data = {
      labels: ['Scatter'],
      datasets: [
        {
          label: 'scatter',
          fill: false,
          backgroundColor: 'rgba(75,192,192,0.4)',
          pointBorderColor: 'rgba(75,192,192,1)',
          pointBackgroundColor: '#fff',
          pointBorderWidth: 1,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: 'rgba(75,192,192,1)',
          pointHoverBorderColor: 'rgba(220,220,220,1)',
          pointHoverBorderWidth: 2,
          pointRadius: 1,
          pointHitRadius: 10,
          data: [
            { x: 0, y: 0 },
          ]
        }
      ]
    };

    request
      .get('http://127.0.0.1:5000/mock_dist_data/2')
      .end((err, res) => {
        if (err) {
          console.log(err);
          return;
        }

        const data = res.body.data;
        this._label = res.body.label;

        this._data.datasets[0].data = res.body.data.map((e: number[]) => {
          return {
            x: e[0],
            y: e[1]
          }
        });

        this.forceUpdate();
      })
  }

  render() {
    return (
      <div>
        <ChartScatter data={this._data} redraw />
      </div>
    )
  }
}

export default Scatter;
