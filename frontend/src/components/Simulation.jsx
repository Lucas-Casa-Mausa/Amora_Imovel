import React, { useState } from 'react';
import api from '../api';
import SimulationForm from './SimulationForm';

const Simulation = () => {
  const [resultado, setResultado] = useState(null);
  const [erro, setErro] = useState('');

  const simular = async (dados) => {
    try {
      const response = await api.post('/simulacao', {
        valor_imovel: parseFloat(dados.valor_imovel),
        percentual_entrada: parseFloat(dados.percentual_entrada),
        anos_contrato: parseInt(dados.anos_contrato, 10)
      });
      setResultado(response.data);
      setErro('');
    } catch (error) {
      console.error('Erro na simulação', error);
      setErro('Erro na simulação. Confira os valores e tente novamente.');
      setResultado(null);
    }
  };

  return (
    <div className="max-w-md mx-auto p-4">
      <h2 className="text-2xl font-bold mb-4">Simulação aMORA</h2>
      <SimulationForm simular={simular} />

      {erro && <p className="text-red-500 mt-4">{erro}</p>}

      {resultado && (
        <div className="mt-6 bg-white p-4 rounded shadow">
          <h3 className="text-xl font-semibold mb-2">Resultado:</h3>
          <p>Valor da entrada: R$ {resultado.valor_entrada.toFixed(2)}</p>
          <p>Valor financiado: R$ {resultado.valor_financiado.toFixed(2)}</p>
          <p>Total a guardar: R$ {resultado.total_a_guardar.toFixed(2)}</p>
          <p>Parcela mensal: R$ {resultado.parcela_mensal.toFixed(2)}</p>
        </div>
      )}
    </div>
  );
};

export default Simulation;