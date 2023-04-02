import STYLES from './Footer.module.scss';

export function Footer() {
  return (
    <div className={STYLES.footer}>
      <div className={STYLES['footer-logo']}>
        <a href="/" className={STYLES.logo} aria-label="Go to the Homepage."><img src="../nzt_logo.png" alt="" height={32} /></a>
      </div>
      <div>
        <div className={STYLES['footer-links-container']}>
          <div className={STYLES['footer-map']}>
            <div className={STYLES['footer-links']}>
              <a href="/history/" aria-label="History">History</a>
            </div>
            <div className={STYLES['footer-links']}>
              <a href="/roll/" aria-label="Company Roll">Company Roll</a>
            </div>
          </div>
          <div className={STYLES['footer-website']}>
            <div className={STYLES['footer-links']}>
              <a href="/about-us/" aria-label="About Us">About Us</a>
            </div>
            <div className={STYLES['footer-links']}>
              <a href="/contact-us/" aria-label="Contact Us">Contact Us</a>
            </div>
            <div className={STYLES['footer-links']}>
              <a href="/help-us/" aria-label="Help Us">Help Us</a>
            </div>
          </div>
          <div className={STYLES['footer-conference']}>
            Next conference
          </div>
        </div>
      </div>
    </div>
  );
}
