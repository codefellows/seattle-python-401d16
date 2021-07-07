import Head from 'next/head'
import Header from '../components/header'
import QuestionForm from '../components/question-form'
import EightBall from '../components/eight-ball'
import Footer from '../components/footer'
import History from '../components/history'
import { useState } from 'react'
import { replies } from '../data'

export default function Home() {

    const [answeredQuestions, setAnsweredQuestions] = useState([]);

    function questionHandler(question) {
        const randIndex = Math.floor(Math.random() * replies.length);
        const reply = replies[randIndex];
        const answeredQuestion = {
            id: answeredQuestions.length + 1,
            question,
            reply,
        };
        setAnsweredQuestions([...answeredQuestions, answeredQuestion]);
    }

    return (
        <div>
            <Head><title>Magic Eight Ball</title></Head>
            <Header answerCount={answeredQuestions.length} />
            <QuestionForm onQuestion={questionHandler} />
            <EightBall answeredQuestion={answeredQuestions[answeredQuestions.length - 1]} />
            <History answeredQuestions={answeredQuestions} />
            <Footer />
        </div>
    )
}
