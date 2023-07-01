import STYLES from './Menu.module.scss';

export function Menu() {
  return (
    <div className={STYLES.menu}>
      <a href="/" className={STYLES.logo} aria-label="Go to the Homepage"><img src="/nzt_logo.png" alt="" /></a>
      <div className={STYLES['search-form']}>
        <form>
          <input type="text" id="search" name="search" placeholder="Search for a tunneller" />
        </form>
        <button type="submit" className={STYLES['search-form-button']}>
          <img src="/searching_hover.png" alt="" height={18} />
        </button>
      </div>
    </div>
  );
}
