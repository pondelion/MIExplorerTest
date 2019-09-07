import React from 'react';
import { slide as BurgerMenu } from 'react-burger-menu';


type Props= {}

export class Menu extends React.Component<Props> {

  render() {
    return (
      <div></div>
      // <BurgerMenu>
      //   <a id="home" className="menu-item" href="/">Home</a>
      //   <a id="about" className="menu-item" href="/about">About</a>
      //   <a id="contact" className="menu-item" href="/contact">Contact</a>
      //   {/* <a onClick={ this.showSettings } className="menu-item--small" href="">Settings</a> */}
      // </BurgerMenu>
    )
  }
}

export default Menu;
