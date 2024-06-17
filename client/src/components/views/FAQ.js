import React, { useState } from 'react';
import '../Styles/FAQ.css';

const FAQItem = ({ question, answer }) => {
    const [isAnswerVisible, setIsAnswerVisible] = useState(false);

    const toggleAnswerVisibility = () => {
        setIsAnswerVisible(!isAnswerVisible);
    };

    return (
        <div>
            <div className='title-line'>
                <h3 className='title'>{question}</h3>
                <div className='symbol' onClick={toggleAnswerVisibility} style={{ cursor: 'pointer', display: 'inline-block', marginLeft: '10px' }}>
                    {isAnswerVisible ? '-' : '+'}
                </div>
            </div>
            {isAnswerVisible && (
                <div className='answer-block'>
                    <p className='answer'>{answer}</p>
                </div>
            )}
        </div>
    );
};

const FAQ = () => {
    const faqData = [
        { question: 'What is the Green Carbon Tracker?', answer: 'The Green Carbon Tracker is a tool to help you monitor and reduce your carbon emissions. It uses advanced algorithms and data analysis to calculate your carbon emissions based on your activities and lifestyle. It takes into account factors such as transportation, energy usage, and consumption patterns.' },
        { question: 'How does the Green Carbon Tracker work?', answer: 'The Green Carbon Tracker uses advanced algorithms and data analysis to calculate your carbon emissions based on your activities and lifestyle. It takes into account factors such as transportation, energy usage, and consumption patterns.' },
        { question: 'Why should I track my carbon emissions?', answer: 'Tracking your carbon emissions is important because it helps you understand the impact of your actions on the environment. By monitoring your emissions, you can identify areas where you can reduce your carbon footprint and make more sustainable choices.' },
        { question: 'Can the Green Carbon Tracker help me reduce my carbon footprint?', answer: 'Yes, the Green Carbon Tracker not only tracks your carbon emissions but also provides recommendations and tips on how to reduce your carbon footprint. It suggests sustainable alternatives and helps you set goals to minimize your impact on the environment.' },
    ];

    return (
        <div className='container'>
            <h2>FAQ</h2>
            {faqData.map((faq, index) => (
                <FAQItem key={index} question={faq.question} answer={faq.answer} />
            ))}
        </div>
    );
};

export default FAQ;