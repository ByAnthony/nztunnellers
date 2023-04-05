import STYLES from './Footer.module.scss';

export function Footer() {
  return (
    <div className={STYLES['footer-content']}>
      <div className={STYLES['footer-logo']}>
        <a href="/" className={STYLES.logo} aria-label="Go to the Homepage."><img src="../nzt_logo.png" alt="" height={42} /></a>
      </div>
    </div>
  );
}
