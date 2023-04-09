import STYLES from './Footer.module.scss';

export function Footer() {
  const handleClick = () => {
    window.scrollTo(0, 0);
  };

  return (
    <div className={STYLES.footer}>
      <div className={STYLES.support}>
        <p>Support</p>
        <div className={STYLES['support-logos']}>
          <a href="https://www.univ-artois.fr/artois-university" aria-label="Go to The Artois University website."><img src="../images/support/logo-univ-artois-blanc_0.png" alt="" /></a>
          <a href="https://www.irsem.fr/en/" aria-label="Go to The Institute for Strategic Research website."><img src="../images/support/irsem-white.png" alt="" /></a>
        </div>
      </div>
      <div className={STYLES.links}>
        <button type="button" className={STYLES['scroll-top']} onClick={handleClick}>&uarr;</button>
      </div>
    </div>
  );
}
