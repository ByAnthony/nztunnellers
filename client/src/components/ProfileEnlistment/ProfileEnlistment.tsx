import STYLES from './ProfileEnlistment.module.scss';

// type Props = {
//     origins: Origins;
// }

export function ProfileEnlistment() {
  return (
    <div className={STYLES.enlistment}>
      <button type="button" key="Enlistment" className={STYLES['profile-button']}>Enlistment</button>
    </div>
  );
}
