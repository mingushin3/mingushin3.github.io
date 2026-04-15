import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from 'recharts';

export default function PKSimulator() {
  // 1. 초기 파라미터 상태 설정 (State)
  const [r0, setR0] = useState(100);       // 투여 속도 (mg/h 등)
  const [clint, setClint] = useState(10);  // 고유청소율 (L/h)
  const [fu, setFu] = useState(0.1);       // 유리분율 (0.01 ~ 1.0)

  // 2. PK 수식에 따른 실시간 농도 계산 (Reactive Logic)
  const css = r0 / (fu * clint); // 총 농도
  const cuss = r0 / clint;       // 유리형 농도

  // 3. 차트에 주입할 데이터 배열
  const data = [
    { name: '총 농도 (C_ss)', value: parseFloat(css.toFixed(1)), color: '#4A90E2' },
    { name: '유리형 농도 (C_u,ss)', value: parseFloat(cuss.toFixed(1)), color: '#E94E77' }
  ];

  return (
    <div style={{ maxWidth: '600px', margin: '0 auto', padding: '20px', fontFamily: 'sans-serif' }}>
      <h2 style={{ textAlign: 'center', color: '#333' }}>경구 투여: 유리분율(fu) 변화 시뮬레이터</h2>
      
      {/* 컨트롤 패널 (슬라이더) */}
      <div style={{ backgroundColor: '#f5f5f5', padding: '20px', borderRadius: '8px', marginBottom: '20px' }}>
        <div style={{ marginBottom: '15px' }}>
          <label>투여 속도 (R0): {r0}</label>
          <input 
            type="range" min="10" max="500" step="10" 
            value={r0} onChange={(e) => setR0(Number(e.target.value))} 
            style={{ width: '100%', display: 'block' }} 
          />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label>고유청소율 (Clint): {clint}</label>
          <input 
            type="range" min="1" max="50" step="1" 
            value={clint} onChange={(e) => setClint(Number(e.target.value))} 
            style={{ width: '100%', display: 'block' }} 
          />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label style={{ fontWeight: 'bold', color: '#d9534f' }}>
            유리분율 (fu): {fu.toFixed(2)}
          </label>
          <input 
            type="range" min="0.01" max="1.0" step="0.01" 
            value={fu} onChange={(e) => setFu(Number(e.target.value))} 
            style={{ width: '100%', display: 'block' }} 
          />
        </div>
      </div>

      {/* 시각화 차트 영역 */}
      <div style={{ height: '300px', width: '100%' }}>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="value" radius={[4, 4, 0, 0]}>
              {data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.color} />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 실시간 수치 결과 텍스트 */}
      <div style={{ marginTop: '20px', textAlign: 'center', fontSize: '18px' }}>
        <p>계산된 총 농도 (Css): <strong>{css.toFixed(2)}</strong></p>
        <p>계산된 유리형 농도 (Cu,ss): <strong>{cuss.toFixed(2)}</strong></p>
      </div>
    </div>
  );
}
