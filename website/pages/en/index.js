/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

const React = require('react');

const CompLibrary = require('../../core/CompLibrary.js');

const MarkdownBlock = CompLibrary.MarkdownBlock; /* Used to read markdown */
const Container = CompLibrary.Container;
const GridBlock = CompLibrary.GridBlock;

class HomeSplash extends React.Component {
  render() {
    const {siteConfig, language = ''} = this.props;
    const {baseUrl, docsUrl} = siteConfig;
    const docsPart = `${docsUrl ? `${docsUrl}/` : ''}`;
    const langPart = `${language ? `${language}/` : ''}`;
    const docUrl = doc => `${baseUrl}${docsPart}${langPart}${doc}`;

    const SplashContainer = props => (
      <div className="homeContainer">
        <div className="homeSplashFade">
          <div className="wrapper homeWrapper">{props.children}</div>
        </div>
      </div>
    );

    const Logo = props => (
      <div className="projectLogo">
        <img src={props.img_src} alt="Project Logo" />
      </div>
    );

    const ProjectTitle = () => (
      <h2 className="projectTitle">
        {siteConfig.title}
        <small>{siteConfig.tagline}</small>
      </h2>
    );

 
    return (
      <SplashContainer>
        <Logo img_src={`${baseUrl}img/undraw_goal.svg`} />
        <div className="inner">
          <ProjectTitle siteConfig={siteConfig} />
          
        </div>
      </SplashContainer>
    );
  }
}

class Index extends React.Component {
  render() {
    const {config: siteConfig, language = ''} = this.props;
    const {baseUrl} = siteConfig;

    const Block = props => (
      <Container
        padding={['bottom', 'top']}
        id={props.id}
        background={props.background}>
        <GridBlock
          align="center"
          contents={props.children}
          layout={props.layout}
        />
      </Container>
    );

    const Features = () => (
      <Block layout="fourColumn" background="light">
        {[
          {
            content: 'Não esquente a cabeça com o sorteio de times, o driblô cuida disso pra você.',
            image: `${baseUrl}img/undraw_team_spirit.svg`,
            imageAlign: 'top',
            title: 'Sorteio de times',
          },
          {
            content: 'Marque o placar e o tempo no driblô',
            image: `${baseUrl}img/undraw_time_management.svg`,
            imageAlign: 'top',
            title: 'Gerenciamento de partidas',
          },
          {
            content: 'A gente cuida do pagamento, dividindo o valor entre os membros da pelada.',
            image: `${baseUrl}img/undraw_wallet.svg`,
            imageAlign: 'top',
            title: 'Gerenciamento de pagamentos',
          },
  

        ]}
      </Block>
    );


    return (
      <div>
        <HomeSplash siteConfig={siteConfig} language={language} />
        <div className="mainContainer">
          <Features />
         
        </div>
      </div>
    );
  }
}

module.exports = Index;
