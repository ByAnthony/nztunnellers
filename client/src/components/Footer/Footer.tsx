import STYLES from './Footer.module.scss';

export function Footer() {
  return (
    <div className={STYLES.footer}>
      <div>
        <a href="/" className={STYLES.logo} aria-label="Go to the Homepage."><img src="../nzt_logo.png" alt="" height={32} /></a>
      </div>
      <div>
        <div className={STYLES['footer-links-container']}>
          <div className={STYLES['footer-links']}>
            <ul>
              <li>
                <a href="/history/" aria-label="History">History</a>
              </li>
              <li>
                <a href="/roll/" aria-label="Company Roll">Company Roll</a>
              </li>
            </ul>

          </div>
          <div className={STYLES['footer-links']}>
            <ul>
              <li>
                <a href="/about-us/" aria-label="About Us">About Us</a>
              </li>
              <li>
                <a href="/contact-us/" aria-label="Contact Us">Contact Us</a>
              </li>
              <li>
                <a href="/help-us/" aria-label="Help Us">Help Us</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
