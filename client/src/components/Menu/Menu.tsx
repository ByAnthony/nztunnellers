import STYLES from './Menu.module.scss';

export function Menu() {
  return (
    <div className={STYLES.menu}>
      <a href="/" aria-label="Go back to homepage"><img src="../nzt_logo.png" alt="" height={32} /></a>
      <div className={STYLES['search-form']}>
        <form>
          <input type="text" id="search" name="search" placeholder="Search for a tunneller" />
        </form>
        <button type="submit" className="search-form__button">
          <img src="../searching_hover.png" alt="" height={18} />
        </button>
      </div>
    </div>
  );
}
