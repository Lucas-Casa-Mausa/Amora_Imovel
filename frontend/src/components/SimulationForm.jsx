import React, { useState } from 'react';

const SimulationForm = ({ simular }) => {
  const [form, setForm] = useState({ valor_imovel: '', percentual_entrada: '', anos_contrato: '' });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    simular(form);
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-4 rounded shadow flex flex-col space-y-4">
      <label className="block">
        <span className="font-medium">Valor do imóvel:</span>
        <input
          type="number"
          name="valor_imovel"
          value={form.valor_imovel}
          onChange={handleChange}
          min="0"
          required
          className="w-full p-2 border rounded mt-1"
        />
      </label>

      <label className="block">
        <span className="font-medium">Percentual de entrada (5 a 20):</span>
        <input
          type="number"
          name="percentual_entrada"
          value={form.percentual_entrada}
          onChange={handleChange}
          min="5"
          max="20"
          required
          className="w-full p-2 border rounded mt-1"
        />
      </label>

      <label className="block">
        <span className="font-medium">Duração do contrato (1 a 5 anos):</span>
        <input
          type="number"
          name="anos_contrato"
          value={form.anos_contrato}
          onChange={handleChange}
          min="1"
          max="5"
          required
          className="w-full p-2 border rounded mt-1"
        />
      </label>

      <button
        type="submit"
        className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700"
      >
        Simular
      </button>
    </form>
  );
};

export default SimulationForm;
