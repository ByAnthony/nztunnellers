import { Link } from 'react-router-dom';
import STYLES from './Footer.module.scss';

export function Footer() {
  const handleClick = () => {
    window.scrollTo(0, 0);
  };

  return (
    <div className={STYLES.footer}>
      <div className={STYLES.support}>
        <div className={STYLES['fullwidth-main-card']}>
          <p>New Zealand Tunnellers Website</p>
          <span>Supported by</span>
        </div>
        <div className={STYLES['halfwidth-cards-container']}>
          <div className={STYLES['halfwidth-secondary-card']}>
            <a href="https://www.univ-artois.fr/artois-university" aria-label="Go to The Artois University website."><img src="/images/support/logo-univ-artois-blanc_0.png" alt="Artois University homepage" /></a>
          </div>
          <div className={STYLES['halfwidth-secondary-card']}>
            <a href="https://www.irsem.fr/en/" aria-label="Go to The Institute for Strategic Research website."><img src="/images/support/irsem-white.png" alt="Institute for Strategic Research homepage" /></a>
          </div>
        </div>
      </div>
      <div className={STYLES.links}>
        <Link to="/contact-us" className={STYLES['fullwidth-main-card']}>
          <p>Contact Us</p>
        </Link>
        <button type="button" className={STYLES['scroll-top']} onClick={handleClick} aria-label="Go back to the top of the page.">&uarr;</button>
      </div>
    </div>
  );
}
